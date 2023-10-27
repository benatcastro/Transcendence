import { HttpService } from '@nestjs/axios';
import { Injectable } from '@nestjs/common';
import { AxiosError, AxiosResponse } from 'axios';
import { Observable, catchError, firstValueFrom, map, tap } from 'rxjs';
import { error, log } from 'console';
import { Prisma, User } from '@prisma/client';
import { JwtService } from '@nestjs/jwt'

@Injectable()
export class AuthService {
    constructor(private readonly httpService: HttpService, private readonly jwtService: JwtService ) {}

    getLoginRedirectURI(): string {
        const RedirectUrl: string = process.env.REDIRECT_URL;
        const API_UID: string = process.env.API_UID;
        return (
            'https://api.intra.42.fr/oauth/authorize?client_id=' +
      API_UID +
      '&redirect_uri=' +
      RedirectUrl +
      '&response_type=code&scope=public' +
      '&state=a_very_long_random_string_witchmust_be_unguessable\''
        );
    }

    async getAccessToken(code: string, state: string): Promise<any> {
        let endpoint = 'https://api.intra.42.fr/oauth/token';

        const client_id :string = process.env.API_UID;
        const client_secret :string = process.env.API_SECRET;
        const redirect_uri: string = process.env.REDIRECT_URL;
        const grant_type = 'authorization_code';

        endpoint +=
      '?grant_type=' +
      grant_type +
      '&client_id=' +
      client_id +
      '&client_secret=' +
      client_secret +
      '&redirect_url' +
      redirect_uri +
      '&code=' +
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
                tap((access_token) => log('token %s', access_token)),
            ),
        );
        return access_token;
    }

    async getUserFromApi(access_token): Promise<any> {
        const endpoint = 'https://api.intra.42.fr/v2/me';

        const config = {
            headers: {
                Authorization: 'Bearer ' + access_token,
            },
        };

        const user: { email; username; auth_type } = await firstValueFrom(
            this.httpService.get(endpoint, config).pipe(
                map((res) => res?.data),
                map((data) => {
                    const email = data?.email;
                    const username = data?.login;
                    const auth_type = '42auth';
                    return { email, username, auth_type };
                }),
            ),
        );
        return user;
    }

    async createJWT( user: User ) {
        const payload = { id: user.id, username: user.id };

        return {
            JWT: this.jwtService.sign(payload),
            ExpiresIn: process.env.JWT_EXPIRES_IN
        }
    }
}