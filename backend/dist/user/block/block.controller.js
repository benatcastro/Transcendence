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
exports.BlockController = void 0;
const common_1 = require("@nestjs/common");
const block_service_1 = require("./block.service");
let BlockController = class BlockController {
    constructor(blockService) {
        this.blockService = blockService;
    }
    async getBlocks(id) {
        return await this.blockService.getBlockedUsers(Number(id));
    }
    async block(id, blockId) {
        const block = await this.blockService.block(Number(id), Number(blockId));
        return block;
    }
    async unblock(id, blockId) {
        const unblock = await this.blockService.unblock(Number(id), Number(blockId));
        return unblock;
    }
};
exports.BlockController = BlockController;
__decorate([
    (0, common_1.Get)(':id'),
    __param(0, (0, common_1.Param)('id')),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [String]),
    __metadata("design:returntype", Promise)
], BlockController.prototype, "getBlocks", null);
__decorate([
    (0, common_1.Post)(':id'),
    __param(0, (0, common_1.Param)('id')),
    __param(1, (0, common_1.Body)('blockId')),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [String, String]),
    __metadata("design:returntype", Promise)
], BlockController.prototype, "block", null);
__decorate([
    (0, common_1.Delete)(':id'),
    __param(0, (0, common_1.Param)('id')),
    __param(1, (0, common_1.Body)('blockId')),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [String, String]),
    __metadata("design:returntype", Promise)
], BlockController.prototype, "unblock", null);
exports.BlockController = BlockController = __decorate([
    (0, common_1.Controller)('block'),
    __metadata("design:paramtypes", [block_service_1.BlockService])
], BlockController);
//# sourceMappingURL=block.controller.js.map