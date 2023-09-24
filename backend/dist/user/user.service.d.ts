import { PrismaService } from "src/prisma/prisma.service";
import { Prisma, User } from "@prisma/client";
export declare class UserService {
    private prisma;
    constructor(prisma: PrismaService);
    all(): Promise<User[]>;
    create(data: Prisma.UserCreateInput): Promise<User>;
}
