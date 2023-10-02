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
exports.UserController = void 0;
const common_1 = require("@nestjs/common");
const common_2 = require("@nestjs/common");
const user_service_1 = require("./user.service");
const console_1 = require("console");
let UserController = class UserController {
    constructor(userService) {
        this.userService = userService;
    }
    async createUser(userData) {
        const users = await this.userService.create(userData);
        if (!users)
            throw new common_1.NotFoundException(`No users found`);
        return users;
    }
    async returnAll() {
        return await this.userService.all();
    }
    async getUserById(id) {
        (0, console_1.log)("entra");
        const user = await this.userService.findById(Number(id));
        if (!user)
            throw new common_1.NotFoundException(`User with id: ${id} does not exist.`);
        return user;
    }
    async getFriends(id) {
        return await this.userService.findFriends(Number(id));
    }
    async addFriend(id, friendId) {
        (0, console_1.log)(id);
        (0, console_1.log)(friendId);
        const result = await this.userService.addFriend(Number(id), Number(friendId));
    }
    async updateEmail(id, email) {
        const update = await this.userService.updateEmail(Number(id), email);
        return update;
    }
    async generalUpdate(id, userData) {
        const update = await this.userService.updateUser(Number(id), userData);
        return update;
    }
    async updateUsername(id, username) {
        const update = await this.userService.updateUsername(Number(id), username);
        return update;
    }
};
exports.UserController = UserController;
__decorate([
    (0, common_2.Post)(),
    __param(0, (0, common_1.Body)()),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [Object]),
    __metadata("design:returntype", Promise)
], UserController.prototype, "createUser", null);
__decorate([
    (0, common_2.Get)(),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", []),
    __metadata("design:returntype", Promise)
], UserController.prototype, "returnAll", null);
__decorate([
    (0, common_2.Get)(':id'),
    __param(0, (0, common_1.Param)('id')),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [String]),
    __metadata("design:returntype", Promise)
], UserController.prototype, "getUserById", null);
__decorate([
    (0, common_2.Get)(':id/friend'),
    __param(0, (0, common_1.Param)('id')),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [String]),
    __metadata("design:returntype", Promise)
], UserController.prototype, "getFriends", null);
__decorate([
    (0, common_2.Post)(':id/friend'),
    __param(0, (0, common_1.Param)('id')),
    __param(1, (0, common_1.Body)('friendId')),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [String, String]),
    __metadata("design:returntype", Promise)
], UserController.prototype, "addFriend", null);
__decorate([
    (0, common_2.Put)('email/:id'),
    __param(0, (0, common_1.Param)('id')),
    __param(1, (0, common_1.Body)()),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [String, String]),
    __metadata("design:returntype", Promise)
], UserController.prototype, "updateEmail", null);
__decorate([
    (0, common_2.Put)(':id'),
    __param(0, (0, common_1.Param)('id')),
    __param(1, (0, common_1.Body)()),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [Number, Object]),
    __metadata("design:returntype", Promise)
], UserController.prototype, "generalUpdate", null);
__decorate([
    (0, common_2.Put)('username/:id'),
    __param(0, (0, common_1.Param)('id')),
    __param(1, (0, common_1.Body)()),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [String, String]),
    __metadata("design:returntype", Promise)
], UserController.prototype, "updateUsername", null);
exports.UserController = UserController = __decorate([
    (0, common_1.Controller)('user'),
    __metadata("design:paramtypes", [user_service_1.UserService])
], UserController);
//# sourceMappingURL=user.controller.js.map