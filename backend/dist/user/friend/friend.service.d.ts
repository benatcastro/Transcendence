import { PrismaService } from 'src/prisma/prisma.service';
export declare class FriendService {
    private prisma;
    constructor(prisma: PrismaService);
    findFriends(id: number): Promise<{
        friends: {
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
    addFriend(id: number, friendId: number): Promise<{
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
    deleteFriend(id: number, friendId: number): Promise<{
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
