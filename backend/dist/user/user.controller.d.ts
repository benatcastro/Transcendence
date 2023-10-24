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
        avatar: string;
        elo: number;
        wins: number;
        loses: number;
        updatedAt: Date;
        createdAt: Date;
    }[]>;
    getUserById(id: string): Promise<{
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
    updateEmail(id: string, email: string): Promise<{
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
    generalUpdate(id: number, userData: {
        email: string;
        username: string;
        auth_type: string;
    }): Promise<{
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
    updateUsername(id: string, username: string): Promise<{
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
    deleteUser(id: string): Promise<{
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
