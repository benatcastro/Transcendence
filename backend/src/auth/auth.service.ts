import { HttpService } from '@nestjs/axios';
import { Injectable } from '@nestjs/common';

@Injectable()
export class AuthService {
  constructor(private readonly httpService:HttpService) {}

    getLoginRedirectURI(): string {
        const RedirectUrl: string = process.env.REDIRECT_URL;;
        const API_UID: string = process.env.API_UID;;
        return ("https://api.intra.42.fr/oauth/authorize?client_id=" + API_UID +
                "&redirect_uri=" + RedirectUrl + 
                "&response_type=code&scope=public" +
                "&state=a_very_long_random_string_witchmust_be_unguessable'");
    }

    postUserAuth(code: string, state: string) {
        
    }

}
