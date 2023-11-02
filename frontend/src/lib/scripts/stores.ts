import { get, writable, type Writable } from "svelte/store";
export const userLogged = writable(false);

const defaultUserParam = {
    id: 0,
    username: "",
}

interface UserParams {
    id: number;
    username: string;
};

class UserStore {
    private attr: Writable<UserParams>;

    constructor () {
        this.attr = writable(defaultUserParam);
    };

    init(userValues: UserParams) {
        this.attr.set(userValues);
    }
    
    private updateStore(userValues: UserParams) {
        return this.attr.set(userValues);
    }

    getId(): number {
        return get(this.attr).id;
    }

    getUsername(): string {
        return get(this.attr).username;
    }

    setUsername(newUsername: string) {
        let tmp = get(this.attr);

        tmp.username = newUsername

        this.updateStore(tmp);
    }
}

export const userState: UserStore  = new UserStore();

