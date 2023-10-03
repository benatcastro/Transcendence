import { PrismaService } from 'src/prisma/prisma.service';
export declare class FriendService {
    private prisma;
    constructor(prisma: PrismaService);
    findFriends(id: number): Promise<({
        friends: {
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
    })[]>;
    addFriend(id: number, friendId: number): Promise<{
        id: number;
        email: string;
        username: string;
        auth_type: string;
    }>;
    deleteFriend(id: number, friendId: number): Promise<{
        id: number;
        email: string;
        username: string;
        auth_type: string;
    }>;
}
