import requests
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:

    location = req.params.get('location')
    if not location:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            location = req_body.get('location')

    if location:
        range_json = requests.post("https://azuredcip.azurewebsites.net/getazuredcipranges", json = {'region':location,'request':'dcip'} ) 
        range = range_json.json()[location]
        format_range = ''
        for i in range:
            format_range += i + '\n' 
        return func.HttpResponse(f"{format_range}")
    else:
        return func.HttpResponse(
             "Please pass a location on the query string or in the request body",
             status_code=400
        )
