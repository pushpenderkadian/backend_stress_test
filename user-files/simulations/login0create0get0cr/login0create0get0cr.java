package login0create0get0cr;

import java.time.Duration;
import java.util.*;

import io.gatling.javaapi.core.*;
import io.gatling.javaapi.http.*;
import io.gatling.javaapi.jdbc.*;

import static io.gatling.javaapi.core.CoreDsl.*;
import static io.gatling.javaapi.http.HttpDsl.*;
import static io.gatling.javaapi.jdbc.JdbcDsl.*;

public class login0create0get0cr extends Simulation {

  private HttpProtocolBuilder httpProtocol = http
    .baseUrl("https://auth.api.edvora.me")
    .inferHtmlResources(AllowList(), DenyList(".*\\.js", ".*\\.css", ".*\\.gif", ".*\\.jpeg", ".*\\.jpg", ".*\\.ico", ".*\\.woff", ".*\\.woff2", ".*\\.(t|o)tf", ".*\\.png", ".*detectportal\\.firefox\\.com.*"))
    .acceptHeader("*/*")
    .acceptEncodingHeader("gzip, deflate")
    .acceptLanguageHeader("en-US,en;q=0.9")
    .userAgentHeader("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36");
  
  private Map<CharSequence, String> headers_0 = Map.ofEntries(
    Map.entry("access-control-request-headers", "content-type"),
    Map.entry("access-control-request-method", "POST"),
    Map.entry("origin", "https://main.edvora.me"),
    Map.entry("pragma", "no-cache"),
    Map.entry("sec-fetch-dest", "empty"),
    Map.entry("sec-fetch-mode", "cors"),
    Map.entry("sec-fetch-site", "same-site")
  );
  
  private Map<CharSequence, String> headers_1 = Map.ofEntries(
    Map.entry("accept", "application/json, text/plain, */*"),
    Map.entry("content-type", "application/json"),
    Map.entry("origin", "https://main.edvora.me"),
    Map.entry("pragma", "no-cache"),
    Map.entry("sec-fetch-dest", "empty"),
    Map.entry("sec-fetch-mode", "cors"),
    Map.entry("sec-fetch-site", "same-site"),
    Map.entry("sec-gpc", "1")
  );
  
  private Map<CharSequence, String> headers_2 = Map.ofEntries(
    Map.entry("accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"),
    Map.entry("pragma", "no-cache"),
    Map.entry("sec-fetch-dest", "document"),
    Map.entry("sec-fetch-mode", "navigate"),
    Map.entry("sec-fetch-site", "none"),
    Map.entry("sec-fetch-user", "?1"),
    Map.entry("sec-gpc", "1"),
    Map.entry("upgrade-insecure-requests", "1")
  );
  
  private Map<CharSequence, String> headers_3 = Map.ofEntries(
    Map.entry("accept", "text/css,*/*;q=0.1"),
    Map.entry("pragma", "no-cache"),
    Map.entry("sec-fetch-dest", "style"),
    Map.entry("sec-fetch-mode", "no-cors"),
    Map.entry("sec-fetch-site", "cross-site"),
    Map.entry("sec-gpc", "1")
  );
  
  private Map<CharSequence, String> headers_4 = Map.ofEntries(
    Map.entry("accept", "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8"),
    Map.entry("pragma", "no-cache"),
    Map.entry("sec-fetch-dest", "image"),
    Map.entry("sec-fetch-mode", "no-cors"),
    Map.entry("sec-fetch-site", "same-origin"),
    Map.entry("sec-gpc", "1")
  );
  
  private Map<CharSequence, String> headers_5 = Map.ofEntries(
    Map.entry("pragma", "no-cache"),
    Map.entry("sec-fetch-dest", "script"),
    Map.entry("sec-fetch-mode", "no-cors"),
    Map.entry("sec-fetch-site", "cross-site"),
    Map.entry("sec-gpc", "1")
  );
  
  private Map<CharSequence, String> headers_6 = Map.ofEntries(
    Map.entry("access-control-request-headers", "authorization"),
    Map.entry("access-control-request-method", "GET"),
    Map.entry("origin", "https://classrooms.edvora.me"),
    Map.entry("pragma", "no-cache"),
    Map.entry("sec-fetch-dest", "empty"),
    Map.entry("sec-fetch-mode", "cors"),
    Map.entry("sec-fetch-site", "same-site")
  );
  
  private Map<CharSequence, String> headers_8 = Map.ofEntries(
    Map.entry("accept", "application/json, text/plain, */*"),
    Map.entry("authorization", "eyJ0b2tlbiI6ImRiYmI2ZTc2LTc2M2EtNDU4YS1iYjhkLWM4ZGM0ZWRkYTA0MiIsInVzZXJuYW1lIjoidGUxIiwib3JnYW5pemF0aW9uX2lkIjoiMTAxIiwic2Vzc2lvbl9pZCI6IjRmOWEwYWQ4LTY5ZWItNGMwZC1hZWEwLTQwNGE3ZWU2MzFhZSIsInJvbGVfaWQiOiI2MjAxMTA1MmFhZGJjYzE0NDJiNGIxNTkifQ=="),
    Map.entry("origin", "https://classrooms.edvora.me"),
    Map.entry("pragma", "no-cache"),
    Map.entry("sec-fetch-dest", "empty"),
    Map.entry("sec-fetch-mode", "cors"),
    Map.entry("sec-fetch-site", "same-site"),
    Map.entry("sec-gpc", "1")
  );
  
  private Map<CharSequence, String> headers_16 = Map.ofEntries(
    Map.entry("access-control-request-headers", "authorization,content-type"),
    Map.entry("access-control-request-method", "POST"),
    Map.entry("origin", "https://classrooms.edvora.me"),
    Map.entry("pragma", "no-cache"),
    Map.entry("sec-fetch-dest", "empty"),
    Map.entry("sec-fetch-mode", "cors"),
    Map.entry("sec-fetch-site", "same-site")
  );
  
  private Map<CharSequence, String> headers_17 = Map.ofEntries(
    Map.entry("accept", "application/json, text/plain, */*"),
    Map.entry("authorization", "eyJ0b2tlbiI6ImFkNTgxMWZhLWRmMzgtNDg4ZS04ZjlhLTIzMDRlYTkzMmFkMSIsInVzZXJuYW1lIjoidGUxIiwib3JnYW5pemF0aW9uX2lkIjoiMTAxIiwic2Vzc2lvbl9pZCI6ImNiYjJiYWZkLTk0NWQtNDBiNy05YmM2LTAyNzgwZDkyMTNiNyIsInJvbGVfaWQiOiI2MjAxMTA1MmFhZGJjYzE0NDJiNGIxNTkifQ=="),
    Map.entry("content-type", "application/json"),
    Map.entry("origin", "https://classrooms.edvora.me"),
    Map.entry("pragma", "no-cache"),
    Map.entry("sec-fetch-dest", "empty"),
    Map.entry("sec-fetch-mode", "cors"),
    Map.entry("sec-fetch-site", "same-site"),
    Map.entry("sec-gpc", "1")
  );
  
  private Map<CharSequence, String> headers_27 = Map.ofEntries(
    Map.entry("accept", "application/json, text/plain, */*"),
    Map.entry("authorization", "eyJ0b2tlbiI6ImQ3NjU5NTAyLTU4NzQtNDBhMi04N2NkLTgzMTEyNzE4YjQ4NyIsInVzZXJuYW1lIjoiVFRUIiwib3JnYW5pemF0aW9uX2lkIjoiMTAxIiwic2Vzc2lvbl9pZCI6Ijk4MGY5NzZiLWE5MWQtNGVmOS1iYzUxLTFiMTgwNzNhYTA0NyIsInJvbGVfaWQiOiI2MjAxMTA1MmFhZGJjYzE0NDJiNGIxNTkifQ=="),
    Map.entry("content-type", "application/json"),
    Map.entry("origin", "https://classrooms.edvora.me"),
    Map.entry("pragma", "no-cache"),
    Map.entry("sec-fetch-dest", "empty"),
    Map.entry("sec-fetch-mode", "cors"),
    Map.entry("sec-fetch-site", "same-site"),
    Map.entry("sec-gpc", "1")
  );
  
  private Map<CharSequence, String> headers_28 = Map.ofEntries(
    Map.entry("accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"),
    Map.entry("pragma", "no-cache"),
    Map.entry("sec-fetch-dest", "document"),
    Map.entry("sec-fetch-mode", "navigate"),
    Map.entry("sec-fetch-site", "same-origin"),
    Map.entry("sec-fetch-user", "?1"),
    Map.entry("sec-gpc", "1"),
    Map.entry("upgrade-insecure-requests", "1")
  );
  
  private Map<CharSequence, String> headers_34 = Map.ofEntries(
    Map.entry("accept", "application/json, text/plain, */*"),
    Map.entry("authorization", "eyJ0b2tlbiI6ImQ3NjU5NTAyLTU4NzQtNDBhMi04N2NkLTgzMTEyNzE4YjQ4NyIsInVzZXJuYW1lIjoiVFRUIiwib3JnYW5pemF0aW9uX2lkIjoiMTAxIiwic2Vzc2lvbl9pZCI6Ijk4MGY5NzZiLWE5MWQtNGVmOS1iYzUxLTFiMTgwNzNhYTA0NyIsInJvbGVfaWQiOiI2MjAxMTA1MmFhZGJjYzE0NDJiNGIxNTkifQ=="),
    Map.entry("origin", "https://classrooms.edvora.me"),
    Map.entry("pragma", "no-cache"),
    Map.entry("sec-fetch-dest", "empty"),
    Map.entry("sec-fetch-mode", "cors"),
    Map.entry("sec-fetch-site", "same-site"),
    Map.entry("sec-gpc", "1")
  );
  
  private String uri1 = "https://main.edvora.me/l";
  
  private String uri2 = "https://classrooms.edvora.me";
  
  private String uri3 = "https://classrooms.api.edvora.me/classrooms";

  private ScenarioBuilder scn = scenario("login0create0get0cr")
    // .exec(
    //   http("request_0:OPTIONS_https://auth.api.edvora.me/login")
    //     .options("/login")
    //     .headers(headers_0)
    //     .resources(
    //       http("request_1:POST_https://auth.api.edvora.me/login")
    //         .post("/login")
    //         .headers(headers_1)
    //         .body(RawFileBody("login0create0get0cr/login0create0get0cr/ac1.json"))
    //     )
    // )
    // .pause(5)
    // .exec(
    //   http("request_2:GET_https://classrooms.edvora.me/")
    //     .get(uri2 + "/")
    //     .headers(headers_2)
    //     .resources(
    //       http("request_14:OPTIONS_https://classrooms.api.edvora.me/classrooms")
    //         .options(uri3)
    //         .headers(headers_6),
    //       http("request_15:GET_https://classrooms.api.edvora.me/classrooms")
    //         .get(uri3)
    //         .headers(headers_8)
    //     )
    // )
    .pause(3)
    .exec(
      http("request_16:OPTIONS_https://classrooms.api.edvora.me/classrooms")
        .options(uri3)
        .headers(headers_16)
        .resources(
          http("create_classroom_request_https://classrooms.api.edvora.me/classrooms")
            .post(uri3)
            .headers(headers_17)
            .body(RawFileBody("login0create0get0cr/login0create0get0cr/ccr1.json"))
        )
    );
    // .pause(3)
    // .exec(
    //   http("request_24:OPTIONS_https://auth.api.edvora.me/login")
    //     .options("/login")
    //     .headers(headers_0)
    //     .resources(
    //       http("request_25:POST_https://auth.api.edvora.me/login")
    //         .post("/login")
    //         .headers(headers_1)
    //         .body(RawFileBody("login0create0get0cr/login0create0get0cr/ac2.json"))
    //     )
    // )
    // .pause(12)
    // .exec(
    //   http("request_26:OPTIONS_https://classrooms.api.edvora.me/classrooms")
    //     .options(uri3)
    //     .headers(headers_16)
    //     .resources(
    //       http("request_27:POST_https://classrooms.api.edvora.me/classrooms")
    //         .post(uri3)
    //         .headers(headers_27)
    //         .body(RawFileBody("login0create0get0cr/login0create0get0cr/ccr2.json"))
    //     )
    // )
    // .pause(6)
    // .exec(
    //   http("request_28:GET_https://classrooms.edvora.me/")
    //     .get(uri2 + "/")
    //     .headers(headers_28)
    //     .resources(
    //       http("request_30:OPTIONS_https://classrooms.api.edvora.me/classrooms")
    //         .options(uri3)
    //         .headers(headers_6),
    //       http("request_34:GET_https://classrooms.api.edvora.me/classrooms")
    //         .get(uri3)
    //         .headers(headers_34)
    //      )
    // );

  {
	  setUp(scn.injectOpen(atOnceUsers(4))).protocols(httpProtocol);
  }
}
