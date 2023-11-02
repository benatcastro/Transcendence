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
var __param = (this && this.__param) || function (paramIndex, decorator) {
    return function (target, key) { decorator(target, key, paramIndex); }
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.AuthController = void 0;
const auth_service_1 = require("./auth.service");
const common_1 = require("@nestjs/common");
const public_decorator_1 = require("../public/public.decorator");
const user_service_1 = require("../user/user.service");
let AuthController = class AuthController {
    constructor(AuthService, UserService) {
        this.AuthService = AuthService;
        this.UserService = UserService;
    }
    redirectToIntraApi(req, res) {
        res.redirect(this.AuthService.getLoginRedirectURI());
    }
    async postUserAuthorization(params) {
        const access_token = await this.AuthService.getAccessToken(params.code, params.state);
        const user_data = await this.AuthService.getUserFromApi(access_token);
        let user;
        user = await this.UserService.findByUsername(user_data.username);
        if (user == null) {
            user = await this.UserService.create(user_data);
        }
        common_1.Logger.log("Issuing JWT for user", user);
        return await this.AuthService.createJWT(user);
    }
    async decrypJWT(authHeader) {
        const [type, token] = authHeader.split(' ') ?? [];
        const payload = await this.AuthService.decryptJWT(token);
        common_1.Logger.log("Payload:", payload);
        return await this.UserService.findById(payload?.id);
    }
};
exports.AuthController = AuthController;
__decorate([
    (0, common_1.Get)('42/login'),
    __param(0, (0, common_1.Req)()),
    __param(1, (0, common_1.Res)()),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [Object, Object]),
    __metadata("design:returntype", void 0)
], AuthController.prototype, "redirectToIntraApi", null);
__decorate([
    (0, common_1.Get)('42/callback'),
    __param(0, (0, common_1.Query)()),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [Object]),
    __metadata("design:returntype", Promise)
], AuthController.prototype, "postUserAuthorization", null);
__decorate([
    (0, common_1.Post)('jwt'),
    __param(0, (0, common_1.Headers)('authorization')),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [String]),
    __metadata("design:returntype", Promise)
], AuthController.prototype, "decrypJWT", null);
exports.AuthController = AuthController = __decorate([
    (0, public_decorator_1.Public)(),
    (0, common_1.Controller)('auth'),
    __metadata("design:paramtypes", [auth_service_1.AuthService,
        user_service_1.UserService])
], AuthController);
//# sourceMappingURL=auth.controller.js.map