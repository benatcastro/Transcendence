import { HttpService } from "@nestjs/axios";
import { AxiosResponse } from "axios";
import { Observable } from "rxjs";
export declare class AuthService {
    private readonly httpService;
    constructor(httpService: HttpService);
    getLoginRedirectURI(): string;
    PostUserAuth(code: string, state: string): Observable<AxiosResponse<string>>;
}
