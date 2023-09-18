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
var _a;
Object.defineProperty(exports, "__esModule", { value: true });
exports.AuthService = void 0;
const axios_1 = require("@nestjs/axios");
const common_1 = require("@nestjs/common");
let AuthService = class AuthService {
    constructor(httpService) {
        this.httpService = httpService;
    }
    getLoginRedirectURI() {
        const RedirectUrl = process.env.REDIRECT_URL;
        ;
        const API_UID = process.env.API_UID;
        ;
        return ("https://api.intra.42.fr/oauth/authorize?client_id=" + API_UID +
            "&redirect_uri=" + RedirectUrl +
            "&response_type=code&scope=public" +
            "&state=a_very_long_random_string_witchmust_be_unguessable'");
    }
    postUserAuth(code, state) {
    }
};
exports.AuthService = AuthService;
exports.AuthService = AuthService = __decorate([
    (0, common_1.Injectable)(),
    __metadata("design:paramtypes", [typeof (_a = typeof axios_1.HttpService !== "undefined" && axios_1.HttpService) === "function" ? _a : Object])
], AuthService);
//# sourceMappingURL=auth.service.js.map