import { AuthService } from './auth.service';
import { Request, Response } from 'express';
export declare class AuthController {
    private readonly AuthService;
    constructor(AuthService: AuthService);
    customRedirect(req: Request, res: Response): void;
    dothings(): string;
}
