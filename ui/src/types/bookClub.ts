import { TMeetingReponse } from "./meeting";
import { TUser } from "./user";


export type TBookClub = {
    name: string;
    book: string;
    previousMeeting?: Date;
    nextMeeting?: Date;
    members?: TUser[];
    id: string;
}

export type TBookClubResponse = {
    name: string;
    id: string;
    meetings?: Array<TMeetingReponse>
}
