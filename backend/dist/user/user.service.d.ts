import { PrismaService } from "src/prisma/prisma.service";
import { Prisma, User } from "@prisma/client";
export declare class UserService {
    private prisma;
    constructor(prisma: PrismaService);
    all(): Promise<User[]>;
    create(data: Prisma.UserCreateInput): Promise<User>;
    getUsernameById(id: number): Promise<string>;
    updateUser(id: number, data: Prisma.UserCreateInput): Promise<{
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
    updateEmail(id: number, email: string): Promise<{
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
    updateUsername(id: number, username: string): Promise<{
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
    findById(id: number): Promise<{
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
    delete(id: number): Promise<{
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
