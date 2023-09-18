import { HttpService } from '@nestjs/axios';
export declare class AuthService {
    private readonly httpService;
    constructor(httpService: HttpService);
    getLoginRedirectURI(): string;
    postUserAuth(code: string, state: string): void;
}
