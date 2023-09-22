import { HttpService } from "@nestjs/axios";
import { Observable } from "rxjs";
export declare class AuthService {
    private readonly httpService;
    constructor(httpService: HttpService);
    getLoginRedirectURI(): string;
    PostUserAuth(code: string, state: string): Observable<string>;
    getUserFromApi(access_token: string): any;
}
