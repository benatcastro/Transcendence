import { constants } from "./constants";

export async function validateJWT( jwt: string ): boolean {
    return true
}

export function isLogged (): boolean {
    if (localStorage.getItem(constants.JWTkey) != undefined && validateJWT("todo"))
        return true;
    return false;
}