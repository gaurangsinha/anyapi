# 🤖 AnyAPI: The API that Makes Up APIs

*Because who needs documentation when you have AI?*



https://github.com/user-attachments/assets/6bbcc49d-aef5-46a6-9e33-e43a1c3dbd1d



## What is this sorcery? 

AnyAPI is a revolutionary tool that turns "I wish I had an API for that" into "I totally have an API for that!" It's basically an API hallucination machine - just point it at any endpoint you wish existed, and watch as GPT pretends it's been there all along!

## Installation 🔧

1. Clone this repository (or just copy-paste the code, we won't judge)
2. Install requirements:
   ```
   pip install bottle openai
   ```
3. Set your OpenAI API key (or use mine, just kidding, please don't)
4. Run the application:
   ```
   python app.py
   ```
5. Point your requests at `http://localhost:8080/whatever/you/want` and marvel at the responses!

## How it works 🤔

1. You send a request to a completely made-up endpoint
2. We forward your gibberish to GPT
3. GPT makes up a reasonable-sounding response
4. You pretend this is a real API
5. Everyone is happy!

## Example Uses 💡

### Weather API That Doesn't Check the Weather
```
GET /weather/forecast?location=timbuktu
```
Response:
```json
{
  "location": "Timbuktu",
  "forecast": "Sunny",
  "temperature": "32°C"
}
```

### Stock Market API That Definitely Shouldn't Be Used for Real Investments
```
GET /stocks/price?symbol=MOON
```
Response:
```json
{
  "symbol": "MOON",
  "price": 42.50
}
```
*Not actually financial advice


### Life Advice API (Accuracy Not Guaranteed)
```
POST /advice/life?problem=existential_crisis
```
Response:
```json
{
  "advice": "Embrace the uncertainty and explore new perspectives to find meaning in your existence."
}
```

### Excuse Generator API
```
GET /excuses/generate?get_out_of=meeting&humor=high
```
Response:
```json
{
  "excuse": "I have a sudden urge to break into an interpretive dance routine, can we reschedule this meeting?"
}
```

## Disclaimer ⚠️

This API will make up responses to anything you ask. Please do not use this!

## Contributing 🤝

Why would you want to contribute to this? But if you insist, pull requests are welcome, especially if they add more humor or unnecessary complexity.

---

*Remember: The best API is the one you don't have to build yourself!*
