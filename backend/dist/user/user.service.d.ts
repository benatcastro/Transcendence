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
    }>;
    updateEmail(id: number, email: string): Promise<{
        id: number;
        email: string;
        username: string;
        auth_type: string;
    }>;
    updateUsername(id: number, username: string): Promise<{
        id: number;
        email: string;
        username: string;
        auth_type: string;
    }>;
    findById(id: number): Promise<{
        id: number;
        email: string;
        username: string;
        auth_type: string;
    }>;
    delete(id: number): Promise<{
        id: number;
        email: string;
        username: string;
        auth_type: string;
    }>;
}
