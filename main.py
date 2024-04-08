from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Flask!'
@app.route("/ussd", methods = ['POST'])
def ussd():
  # Read the variables sent via POST from our API
  session_id   = request.values.get("sessionId", None)
  serviceCode  = request.values.get("serviceCode", None)
  phone_number = request.values.get("phoneNumber", None)
  text         = request.values.get("text", "default")
  print("phone number", phone_number)



  if text == '':
    # This is the first request. Note how we start the response with CON
    response  = "CON Welcome to the platform, kindly pick your preferred option \n"
    response += "1. Nairobi Traffic Services \n"
    response += "2. Learn about what we're doing to aid traffic conditions in Nairobi \n" 

  elif text == '1':
    # Business logic for first level response
    response  = "CON Please Choose your specific Service \n"
    response += "1. Traffic Conditions \n"
    response += "2. Parking \n"
    response += "3. View Weather Conditions \n"
    response += "4. Report an Incident e.g Fatal accident on Moi Av.\n"  

  elif text == '1*1':
    # Business logic for third level response
    response = "END  From our Info, the traffic flow exiting Nairobi is moderate, Expect 15+ min Delays \n"
    return response

  elif text == '1*2':
    # Business logic for third level response
    response = "END Acccording to our info all major parking hubs are available as Traffic is flowing away from the city  \n"
    return response

  elif text == '1*3':
    # Business logic for third level response
    response = "END The NBO Region is projected to have 20mm of rainfall in April , possibility of flood"
    return response

  elif text == '1*4':
    # Business logic for third level response
    response = "CON Submit Input e.g Train accident at Kasarani \n"
    return response

  elif text == '':
    response= "END Info Submitted successfully, Necessary Authorities will be notified \n" 


  elif text == '2':
    # Business logic for second level response
    response = "END   To get detailed Nairobi Traffic Info visit www.GroupZeroTraffic.co.ke  or text our WhatsApp bot on +254745665647\n" 



  else:
    # Default fallback response
    response = "END Invalid input, please try again"

  # Print the response to the console for debugging
  print(response)




  # Return the response to the API
  return response


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
