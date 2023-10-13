"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.AuthService = void 0;
const axios_1 = require("@nestjs/axios");
const common_1 = require("@nestjs/common");
const rxjs_1 = require("rxjs");
const console_1 = require("console");
let AuthService = class AuthService {
    constructor(httpService) {
        this.httpService = httpService;
    }
    getLoginRedirectURI() {
        const RedirectUrl = process.env.REDIRECT_URL;
        const API_UID = process.env.API_UID;
        return ('https://api.intra.42.fr/oauth/authorize?client_id=' +
            API_UID +
            '&redirect_uri=' +
            RedirectUrl +
            '&response_type=code&scope=public' +
            '&state=a_very_long_random_string_witchmust_be_unguessable\'');
    }
    async getAccessToken(code, state) {
        let endpoint = 'https://api.intra.42.fr/oauth/token';
        const client_id = process.env.API_UID;
        const client_secret = process.env.API_SECRET;
        const redirect_uri = process.env.REDIRECT_URL;
        const grant_type = 'authorization_code';
        endpoint +=
            '?grant_type=' +
                grant_type +
                '&client_id=' +
                client_id +
                '&client_secret=' +
                client_secret +
                '&redirect_url' +
                redirect_uri +
                '&code=' +
                code;
        const queryParams = {
            grant_type,
            client_id,
            client_secret,
            code,
            redirect_uri,
        };
        const access_token = await (0, rxjs_1.firstValueFrom)(this.httpService.post(endpoint).pipe((0, rxjs_1.map)((resp) => resp.data?.access_token), (0, rxjs_1.tap)((access_token) => (0, console_1.log)('token %s', access_token))));
        return access_token;
    }
    async getUserFromApi(access_token) {
        const endpoint = 'https://api.intra.42.fr/v2/me';
        const config = {
            headers: {
                Authorization: 'Bearer ' + access_token,
            },
        };
        const user = await (0, rxjs_1.firstValueFrom)(this.httpService.get(endpoint, config).pipe((0, rxjs_1.map)((res) => res?.data), (0, rxjs_1.map)((data) => {
            const email = data?.email;
            const username = data?.login;
            const auth_type = '42auth';
            return { email, username, auth_type };
        })));
        return user;
    }
};
exports.AuthService = AuthService;
exports.AuthService = AuthService = __decorate([
    (0, common_1.Injectable)(),
    __metadata("design:paramtypes", [axios_1.HttpService])
], AuthService);
//# sourceMappingURL=auth.service.js.map