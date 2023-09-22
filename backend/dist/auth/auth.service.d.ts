import { HttpService } from "@nestjs/axios";
export declare class AuthService {
    private readonly httpService;
    constructor(httpService: HttpService);
    getLoginRedirectURI(): string;
    PostUserAuth(code: string, state: string): Promise<any>;
    getUserAccessToken(code: string, state: string): void;
    getUserFromApi(access_token: string): any;
}
