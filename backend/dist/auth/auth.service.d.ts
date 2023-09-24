import { HttpService } from "@nestjs/axios";
export declare class AuthService {
    private readonly httpService;
    constructor(httpService: HttpService);
    getLoginRedirectURI(): string;
    getAccessToken(code: string, state: string): Promise<any>;
    getUserFromApi(access_token: string): Promise<any>;
}
