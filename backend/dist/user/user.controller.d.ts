import { UserService } from './user.service';
import { User } from '@prisma/client';
export declare class UserController {
    private readonly userService;
    constructor(userService: UserService);
    createUser(userData: {
        email: string;
        username: string;
        auth_type: string;
    }): Promise<User>;
    returnAll(): Promise<{
        id: number;
        email: string;
        username: string;
        auth_type: string;
    }[]>;
    getUserById(id: string): Promise<{
        id: number;
        email: string;
        username: string;
        auth_type: string;
    }>;
    updateEmail(id: string, email: string): Promise<{
        id: number;
        email: string;
        username: string;
        auth_type: string;
    }>;
    generalUpdate(id: number, userData: {
        email: string;
        username: string;
        auth_type: string;
    }): Promise<{
        id: number;
        email: string;
        username: string;
        auth_type: string;
    }>;
    updateUsername(id: string, username: string): Promise<{
        id: number;
        email: string;
        username: string;
        auth_type: string;
    }>;
}
