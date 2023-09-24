import { UserService } from "./user.service";
import { User } from "@prisma/client";
export declare class UserController {
    private readonly userService;
    constructor(userService: UserService);
    createUser(userData: {
        email: string;
        username: string;
        auth_type: string;
    }): Promise<User>;
    returnAll(): Promise<{
        id: number;
        email: string;
        username: string;
        auth_type: string;
    }[]>;
}
