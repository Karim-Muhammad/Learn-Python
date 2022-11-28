def whatIsWeather(state):
  match state:
    case "rain":
      print("Pick an umbrella")
    case "thunderstorm":
      print("Don't go out!")
    case "sunny":
      print("pick a Sunglass")
    case "cold":
      print("pick a jacket")
    case _:
      print("what is weather?!")

whatIsWeather("rain");