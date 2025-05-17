
#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";

const char* serverName = "http://your_server_ip:5000/data";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverName);
    http.addHeader("Content-Type", "application/json");

    // Simulated sensor data
    String jsonData = "{"temperature":38.6,"heartbeat":72,"motion":1}";

    int httpResponseCode = http.POST(jsonData);
    Serial.println(httpResponseCode);
    http.end();
  }

  delay(5000); // Post every 5 seconds
}
