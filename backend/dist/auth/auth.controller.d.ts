import { AuthService } from './auth.service';
import { Request, Response } from 'express';
import { UserService } from 'src/user/user.service';
export declare class AuthController {
    private readonly AuthService;
    private readonly UserService;
    constructor(AuthService: AuthService, UserService: UserService);
    redirectToIntraApi(req: Request, res: Response): void;
    postUserAuthorization(params: any): Promise<{
        id: number;
        email: string;
        username: string;
        auth_type: string;
        avatar: string;
        elo: number;
        wins: number;
        loses: number;
        updatedAt: Date;
        createdAt: Date;
    }>;
}
