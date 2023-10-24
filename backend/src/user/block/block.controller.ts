import { Controller, Get, Post, Delete, Body, Param } from '@nestjs/common';
import { BlockService } from './block.service';

@Controller('block')
export class BlockController {
    constructor(private readonly blockService: BlockService) {}

  @Get(':id')
  async getBlocks(@Param('id') id: string) {
    return await this.blockService.getBlockedUsers(Number(id));
  }

  @Post(':id')
  async block(@Param('id') id: string, @Body('blockId') blockId: string) {
    const block = await this.blockService.block(Number(id), Number(blockId));

    return block;
  }

  @Delete(':id')
  async unblock(@Param('id') id: string, @Body('blockId') blockId: string) {

    const unblock = await this.blockService.unblock(Number(id), Number(blockId));

    return unblock;
  }

}