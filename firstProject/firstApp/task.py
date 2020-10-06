def json_response(request,status,status_code,data,message):
    response = {
        'status':status,
        'status_code':status_code,
        'data':data,
        'message':message
    }

    return response
