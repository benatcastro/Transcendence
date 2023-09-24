import { HttpService } from "@nestjs/axios";
import { Injectable } from "@nestjs/common";
import { AxiosError, AxiosResponse } from "axios";
import { Observable, catchError, firstValueFrom, map, tap } from "rxjs";
import { error, log } from "console";

@Injectable()
export class AuthService {
  constructor(private readonly httpService: HttpService) {}

  getLoginRedirectURI(): string {
    const RedirectUrl: string = process.env.REDIRECT_URL;
    const API_UID: string = process.env.API_UID;
    return (
      "https://api.intra.42.fr/oauth/authorize?client_id=" +
      API_UID +
      "&redirect_uri=" +
      RedirectUrl +
      "&response_type=code&scope=public" +
      "&state=a_very_long_random_string_witchmust_be_unguessable'"
    );
  }

    async getAccessToken(code: string, state: string): Promise<any> {

    let endpoint = "https://api.intra.42.fr/oauth/token";

    const client_id = process.env.API_UID;
    const client_secret = process.env.API_SECRET;
    const redirect_uri = process.env.REDIRECT_URL;
    const grant_type = "authorization_code";

    endpoint +=
      "?grant_type=" +
      grant_type +
      "&client_id=" +
      client_id +
      "&client_secret=" +
      client_secret +
      "&redirect_url" +
      redirect_uri +
      "&code=" +
      code;

    const queryParams = {
      grant_type,
      client_id,
      client_secret,
      code,
      redirect_uri,
      // state,
    };

    // log(endpoint);
    const access_token = await firstValueFrom(
      this.httpService.post(endpoint).pipe(
        map((resp) => resp.data?.access_token),
        tap((access_token) => log("token %s", access_token)),
      ));
    return access_token;
  }

  async getUserFromApi(access_token: string): Promise<any> {
    const endpoint = "https://api.intra.42.fr/v2/me";

    const config = {
      headers: {
        Authorization: "Bearer " + access_token,
      }
    }    
    const user = await firstValueFrom(
      this.httpService.get(endpoint, config).pipe(
        map((res) => { return res.data })
      )
    )
    return user;
  }

}
