import json, sys, random

def lambda_handler(event, context):

    errorMessage = "Sorry, we encountered a problem. Please try again."

    #Load interactions
    try:
        f = open("interactions.json", "r")
        interactions = json.loads(f.read())
        f.close()
    except Exception as e:
        print(f"Error: {e}")
        return {
            "statusCode": 500,
            "body": errorMessage
        }

    #Get input
    try:
        inputString = event["queryStringParameters"]["inputString"]
        if inputString == "":
            return {
                "statusCode": 200,
                "body": "Sorry, it looks like you didn't say anything. Please try again."
            }
    except Exception as e:
        print(f"Error: {e}")
        return {
            "statusCode": 400,
            "body": errorMessage
        }
    print("########### New Input ###########")
    print(f"Input String: {inputString}")

    #Work out response
    response = ""
    for interaction, phrases in interactions["interactions"].items():
        for phrase in phrases:
            if phrase in inputString.lower():
                if interaction == "operators":
                    raise NotImplementedError
                else:
                    if interaction == "greetings":
                        responses = ["Hey!", "Hi!", "Hi", "Good day"]
                    elif interaction == "closings":
                        responses = ["Goodbye", "Bye", "See you"]
                    response = responses[random.randint(0, len(responses)-1)]
    if response == "":
        response = "Sorry, I don't know how to respond. Please try again."
    
    print(f"Reponse: {response}")

    #Log response in DDB

    #Return response to user
    return {
        "statusCode": 200,
        "body": response
    }