import { PrismaService } from 'src/prisma/prisma.service';
export declare class BlockService {
    private prisma;
    constructor(prisma: PrismaService);
    getBlockedUsers(id: number): Promise<{
        blocks: {
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
        }[];
    } & {
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
    block(id: number, blockId: number): Promise<{
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
    unblock(id: number, blockId: number): Promise<{
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
