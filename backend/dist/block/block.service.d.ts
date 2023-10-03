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
        }[];
    } & {
        id: number;
        email: string;
        username: string;
        auth_type: string;
    }>;
    block(id: number, blockId: number): Promise<{
        id: number;
        email: string;
        username: string;
        auth_type: string;
    }>;
    unblock(id: number, blockId: number): Promise<{
        id: number;
        email: string;
        username: string;
        auth_type: string;
    }>;
}
