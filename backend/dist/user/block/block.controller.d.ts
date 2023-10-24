import { BlockService } from './block.service';
export declare class BlockController {
    private readonly blockService;
    constructor(blockService: BlockService);
    getBlocks(id: string): Promise<{
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
    block(id: string, blockId: string): Promise<{
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
    unblock(id: string, blockId: string): Promise<{
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
