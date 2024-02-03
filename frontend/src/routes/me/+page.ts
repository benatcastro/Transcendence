
import {get_user_and_refresh} from "$lib/utilities/utilities";
export async function load(){


    const data = async () => {
        return await get_user_and_refresh();
    }
    return await data()
}
