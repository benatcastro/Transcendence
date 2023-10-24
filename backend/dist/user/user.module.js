"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.UserModule = void 0;
const common_1 = require("@nestjs/common");
const user_controller_1 = require("./user.controller");
const user_service_1 = require("./user.service");
const prisma_service_1 = require("../prisma/prisma.service");
const friend_controller_1 = require("./friend/friend.controller");
const friend_service_1 = require("./friend/friend.service");
const block_controller_1 = require("./block/block.controller");
const block_service_1 = require("./block/block.service");
let UserModule = class UserModule {
};
exports.UserModule = UserModule;
exports.UserModule = UserModule = __decorate([
    (0, common_1.Module)({
        controllers: [user_controller_1.UserController, friend_controller_1.FriendController, block_controller_1.BlockController],
        providers: [prisma_service_1.PrismaService, user_service_1.UserService, friend_service_1.FriendService, block_service_1.BlockService],
        exports: [user_service_1.UserService]
    })
], UserModule);
//# sourceMappingURL=user.module.js.map