import json

import elasticsearch
import requests

ID_CREDENTIALS = "rKORoexkrfgZYPI1ScyMg1kzd2u266szTPq9nbSA"
PASS_CREDENTIALS = ""


def scraper_from_UPC():
    response = requests.get('https://api.fib.upc.edu/v2/assignatures/?format=json;lang=en;client_id=' + ID_CREDENTIALS)
    return response


def get_courses(url_response):
    # print(url_response)
    courses = dict()
    i = 0
    results = url_response.json()["results"]
    for result in results:
        course_url = result["guia"]
        if course_url is None:
            continue
        content = course_url + ';lang=en;client_id=' + ID_CREDENTIALS
        course_response = requests.get(content).json()
        course_id = course_response["id"]
        if course_id == "AC":
            print()
        objectives = course_response["objectius"]
        course_objectives = []
        for objective in objectives:
            course_objectives.append(objective["valor"])

        contents = course_response["continguts"]
        course_contents = []
        for content in contents:
            course_contents.append(content["nom"])

        # TODO activities
        professors = course_response["professors"]
        course_professors = []
        for prof in professors:
            course_professors.append(prof["nom"])

        course_name = course_response["nom"]
        course_description = course_response["descripcio"]

        courses[course_name] = {"course_id": course_id, "course_description": course_description,
                                "professors": course_professors.__str__(),
                                "contents": course_contents.__str__(), "objectives": course_objectives.__str__()}
        print(i)
        i += 1

    return courses


def load_as_json(data):
    with open('data.json', 'w') as f:
        json.dump(data, f)


def load_from_json(json_file):
    return json.load(json_file)


def read_password():
    with open('pwd.txt', 'r') as f:
        return f.readlines()[0].strip()


def connect_elastic():
    client = elasticsearch.Elasticsearch(
        "https://localhost:9200",
        ca_certs="./http_ca.crt",
        basic_auth=("elastic", read_password())
    )
    return client


def create_elastic():
    client = connect_elastic()

    upc_mapping = {
        "properties": {
            "name": {"type": "text"},
            "id": {"type": "keyword"},
            "description": {"type": "text"},
            "professors": {"type": "text"},
            "contents": {"type": "text"},
            "objectives": {"type": "text"}
        }
    }

    client.indices.create(index='upc_courses3', mappings=upc_mapping)

    return client


def load_to_es(client, courses):
    for course_name in courses.keys():
        course = courses[course_name]
        course_id = course["course_id"]
        course_description = course["course_description"]
        course_profs = course["professors"]
        course_content = course["contents"]
        course_objectives = course["objectives"]

        doc = {
            "name": course_name,
            "id": course_id,
            "description": course_description,
            "professors": course_profs,
            "contents": course_content,
            "objectives": course_objectives,

        }
        client.index(index="upc_courses3", document=doc)


def course_search(query_string):
    client = connect_elastic()
    query_id = {
            "bool": {
                "filter":
                    {"term": {"id": query_string}}
            }
        }

    query_name = {
        "match": {
            "name": query_string
        }
    }

    query_description = {
        "match": {
            "description": query_string
        }
    }
    results1 = client.search(index="upc_courses3", query=query_id)
    results2 = client.search(index="upc_courses3", query=query_name)
    results3 = client.search(index="upc_courses3", query=query_description)

    return results1["hits"]["hits"]+results2["hits"]["hits"]+results3["hits"]["hits"]


if __name__ == '__main__':
    # scraper
    # json_response = scraper_from_UPC()
    # upc_courses = get_courses(json_response)
    # load_as_json(upc_courses)

    # elasticsearch
    # delete_index("upc_courses")
    # clt = create_elastic()
    # load_to_es(clt, upc_courses)

    course_search("mathematics")
