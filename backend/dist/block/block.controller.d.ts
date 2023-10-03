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
        }[];
    } & {
        id: number;
        email: string;
        username: string;
        auth_type: string;
    }>;
    block(id: string, blockId: string): Promise<{
        id: number;
        email: string;
        username: string;
        auth_type: string;
    }>;
    unblock(id: string, blockId: string): Promise<{
        id: number;
        email: string;
        username: string;
        auth_type: string;
    }>;
}
