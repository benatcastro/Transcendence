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
exports.UserService = void 0;
const common_1 = require("@nestjs/common");
const prisma_service_1 = require("../prisma/prisma.service");
let UserService = class UserService {
    constructor(prisma) {
        this.prisma = prisma;
    }
    async all() {
        return this.prisma.user.findMany();
    }
    async create(data) {
        return this.prisma.user.create({ data });
    }
    async getUsernameById(id) {
        return (await this.findById(id)).username;
    }
    async updateUser(id, data) {
        return this.prisma.user.update({
            where: { id: id },
            data: data,
        });
    }
    async updateEmail(id, email) {
        return this.prisma.user.update({
            where: { id: id },
            data: { email: email },
        });
    }
    async updateUsername(id, username) {
        return this.prisma.user.update({
            where: { id: id },
            data: { username: username },
        });
    }
    async findById(id) {
        return this.prisma.user.findUnique({
            where: { id: id },
        });
    }
    async findFriends(id) {
        return this.prisma.user.findMany({
            where: { id: id },
            include: { friends: true }
        });
    }
    async addFriend(id, friendId) {
        return this.prisma.user.update({
            where: { id: id },
            data: {
                friends: {
                    connect: {
                        id: friendId,
                    }
                }
            }
        });
    }
    async deleteFriend(id, friendId) {
        return this.prisma.user.update({
            where: { id: id },
            data: {
                friends: {
                    delete: {
                        id: friendId,
                    }
                }
            }
        });
    }
};
exports.UserService = UserService;
exports.UserService = UserService = __decorate([
    (0, common_1.Injectable)(),
    __metadata("design:paramtypes", [prisma_service_1.PrismaService])
], UserService);
//# sourceMappingURL=user.service.js.map