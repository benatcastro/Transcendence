import { FriendService } from './friend.service';
export declare class FriendController {
    private readonly friendService;
    constructor(friendService: FriendService);
    getFriends(id: string): Promise<{
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
    addFriend(id: string, friendId: string): Promise<{
        first_add: {
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
        };
        second_add: {
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
        };
    }>;
    deleteFriend(id: string, friendId: string): Promise<{
        first_deletion: {
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
        };
        second_deletion: {
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
        };
    }>;
}
