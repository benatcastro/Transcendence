import { AuthService } from './auth.service';
import { Request, Response } from 'express';
export declare class AuthController {
    private readonly AuthService;
    constructor(AuthService: AuthService);
    redirectToIntraApi(req: Request, res: Response): void;
    postUserAuthorization(params: any): void;
}
