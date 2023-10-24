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
exports.FriendController = void 0;
const common_1 = require("@nestjs/common");
const friend_service_1 = require("./friend.service");
let FriendController = class FriendController {
    constructor(friendService) {
        this.friendService = friendService;
    }
    async getFriends(id) {
        return await this.friendService.findFriends(Number(id));
    }
    async addFriend(id, friendId) {
        const first = Number(id);
        const second = Number(friendId);
        const first_add = await this.friendService.addFriend(first, second);
        const second_add = await this.friendService.addFriend(second, first);
        return { first_add, second_add };
    }
    async deleteFriend(id, friendId) {
        const first = Number(id);
        const second = Number(friendId);
        const first_deletion = await this.friendService.deleteFriend(first, second);
        const second_deletion = await this.friendService.deleteFriend(second, first);
        return { first_deletion, second_deletion };
    }
};
exports.FriendController = FriendController;
__decorate([
    (0, common_1.Get)(':id'),
    __param(0, (0, common_1.Param)('id')),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [String]),
    __metadata("design:returntype", Promise)
], FriendController.prototype, "getFriends", null);
__decorate([
    (0, common_1.Post)(':id'),
    __param(0, (0, common_1.Param)('id')),
    __param(1, (0, common_1.Body)('friendId')),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [String, String]),
    __metadata("design:returntype", Promise)
], FriendController.prototype, "addFriend", null);
__decorate([
    (0, common_1.Delete)(':id'),
    __param(0, (0, common_1.Param)('id')),
    __param(1, (0, common_1.Body)('friendId')),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [String, String]),
    __metadata("design:returntype", Promise)
], FriendController.prototype, "deleteFriend", null);
exports.FriendController = FriendController = __decorate([
    (0, common_1.Controller)('friend'),
    __metadata("design:paramtypes", [friend_service_1.FriendService])
], FriendController);
//# sourceMappingURL=friend.controller.js.map