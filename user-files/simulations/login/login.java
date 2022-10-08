package login;

import java.time.Duration;
import java.util.*;

import io.gatling.javaapi.core.*;
import io.gatling.javaapi.http.*;
import io.gatling.javaapi.jdbc.*;

import static io.gatling.javaapi.core.CoreDsl.*;
import static io.gatling.javaapi.http.HttpDsl.*;
import static io.gatling.javaapi.jdbc.JdbcDsl.*;

public class login extends Simulation {

  {
    HttpProtocolBuilder httpProtocol = http
      .baseUrl("https://auth.api.edvora.me")
      .inferHtmlResources(AllowList(), DenyList(".*\\.js", ".*\\.css", ".*\\.gif", ".*\\.jpeg", ".*\\.jpg", ".*\\.ico", ".*\\.woff", ".*\\.woff2", ".*\\.(t|o)tf", ".*\\.png", ".*detectportal\\.firefox\\.com.*"))
      .acceptHeader("application/json, text/plain, */*")
      .acceptEncodingHeader("gzip, deflate")
      .acceptLanguageHeader("en-US,en;q=0.9")
      .userAgentHeader("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36");
    
    Map<CharSequence, String> headers_0 = new HashMap<>();
    headers_0.put("accept", "*/*");
    headers_0.put("access-control-request-headers", "content-type");
    headers_0.put("access-control-request-method", "POST");
    headers_0.put("origin", "https://main.edvora.me");
    headers_0.put("pragma", "no-cache");
    headers_0.put("sec-fetch-dest", "empty");
    headers_0.put("sec-fetch-mode", "cors");
    headers_0.put("sec-fetch-site", "same-site");
    
    Map<CharSequence, String> headers_1 = new HashMap<>();
    headers_1.put("content-type", "application/json");
    headers_1.put("origin", "https://main.edvora.me");
    headers_1.put("pragma", "no-cache");
    headers_1.put("sec-fetch-dest", "empty");
    headers_1.put("sec-fetch-mode", "cors");
    headers_1.put("sec-fetch-site", "same-site");
    headers_1.put("sec-gpc", "1");
    
    Map<CharSequence, String> headers_2 = new HashMap<>();
    headers_2.put("accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8");
    headers_2.put("pragma", "no-cache");
    headers_2.put("sec-fetch-dest", "document");
    headers_2.put("sec-fetch-mode", "navigate");
    headers_2.put("sec-fetch-site", "none");
    headers_2.put("sec-fetch-user", "?1");
    headers_2.put("sec-gpc", "1");
    headers_2.put("upgrade-insecure-requests", "1");
    
    Map<CharSequence, String> headers_3 = new HashMap<>();
    headers_3.put("accept", "text/css,*/*;q=0.1");
    headers_3.put("pragma", "no-cache");
    headers_3.put("sec-fetch-dest", "style");
    headers_3.put("sec-fetch-mode", "no-cors");
    headers_3.put("sec-fetch-site", "cross-site");
    headers_3.put("sec-gpc", "1");
    
    String uri1 = "https://main.edvora.me/l";
    
    String uri3 = "https://fonts.googleapis.com/css2";

    ScenarioBuilder scn = scenario("login")
      .exec(
        http("request_0:OPTIONS_https://auth.api.edvora.me/login")
          .options("/login")
          .headers(headers_0)
          .resources(
            http("request_1:POST_https://auth.api.edvora.me/login")
              .post("/login")
              .headers(headers_1)
              .body(RawFileBody("login/login/0001_request.json"))
          )
      )
      .pause(3)
      .exec(
        http("request_2:GET_https://main.edvora.me/l")
          .get(uri1)
          .headers(headers_2)
          .resources(
            http("request_3:GET_https://fonts.googleapis.com/css2?family=Inter:wght_100_200_300_400_500_600_700_800_900&display=swap")
              .get(uri3 + "?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap")
              .headers(headers_3)
          )
      )
      .pause(13)
      .exec(
        http("request_4:OPTIONS_https://auth.api.edvora.me/login")
          .options("/login")
          .headers(headers_0)
          .resources(
            http("request_5:POST_https://auth.api.edvora.me/login")
              .post("/login")
              .headers(headers_1)
              .body(RawFileBody("login/login/0005_request.txt"))
              .check(status().is(404))
          )
      )
      .pause(1)
      .exec(
        http("request_6:OPTIONS_https://auth.api.edvora.me/login")
          .options("/login")
          .headers(headers_0)
          .resources(
            http("request_7:POST_https://auth.api.edvora.me/login")
              .post("/login")
              .headers(headers_1)
              .body(RawFileBody("login/login/0007_request.txt"))
              .check(status().is(404)),
            http("request_8:OPTIONS_https://auth.api.edvora.me/login")
              .options("/login")
              .headers(headers_0),
            http("request_9:POST_https://auth.api.edvora.me/login")
              .post("/login")
              .headers(headers_1)
              .body(RawFileBody("login/login/0009_request.txt"))
              .check(status().is(404))
          )
      )
      .pause(3)
      .exec(
        http("request_10:OPTIONS_https://auth.api.edvora.me/login")
          .options("/login")
          .headers(headers_0)
          .resources(
            http("request_11:POST_https://auth.api.edvora.me/login")
              .post("/login")
              .headers(headers_1)
              .body(RawFileBody("login/login/0011_request.json"))
          )
      )
      .pause(2)
      .exec(
        http("request_12:GET_https://main.edvora.me/l")
          .get(uri1)
          .headers(headers_2)
          .resources(
            http("request_13:GET_https://fonts.googleapis.com/css2?family=Inter:wght_100_200_300_400_500_600_700_800_900&display=swap")
              .get(uri3 + "?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap")
              .headers(headers_3)
          )
      )
      .pause(6)
      .exec(
        http("request_14:OPTIONS_https://auth.api.edvora.me/login")
          .options("/login")
          .headers(headers_0)
          .resources(
            http("request_15:POST_https://auth.api.edvora.me/login")
              .post("/login")
              .headers(headers_1)
              .body(RawFileBody("login/login/0015_request.json"))
          )
      );

	  setUp(scn.injectOpen(atOnceUsers(1))).protocols(httpProtocol);
  }
}
