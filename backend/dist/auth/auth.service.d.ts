import { HttpService } from '@nestjs/axios';
import { User } from '@prisma/client';
import { JwtService } from '@nestjs/jwt';
export declare class AuthService {
    private readonly httpService;
    private readonly jwtService;
    constructor(httpService: HttpService, jwtService: JwtService);
    getLoginRedirectURI(): string;
    getAccessToken(code: string, state: string): Promise<any>;
    getUserFromApi(access_token: any): Promise<any>;
    createJWT(user: User): Promise<{
        JWT: string;
        ExpiresIn: string;
    }>;
    decryptJWT(jwt: string): Promise<any>;
}
