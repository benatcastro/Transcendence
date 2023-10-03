import { FriendService } from './friend.service';
export declare class FriendController {
    private readonly friendService;
    constructor(friendService: FriendService);
    getFriends(id: string): Promise<({
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
    addFriend(id: string, friendId: string): Promise<{
        first_add: {
            id: number;
            email: string;
            username: string;
            auth_type: string;
        };
        second_add: {
            id: number;
            email: string;
            username: string;
            auth_type: string;
        };
    }>;
    deleteFriend(id: string, friendId: string): Promise<{
        first_deletion: {
            id: number;
            email: string;
            username: string;
            auth_type: string;
        };
        second_deletion: {
            id: number;
            email: string;
            username: string;
            auth_type: string;
        };
    }>;
}
