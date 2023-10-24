import { Controller, Param, Body, Post, Delete, Get } from '@nestjs/common';
import { FriendService } from './friend.service';

@Controller('friend')
export class FriendController {
  constructor(private readonly friendService: FriendService) {}

  @Get(':id')
  async getFriends(@Param('id') id: string) {
    return await this.friendService.findFriends(Number(id));
  }

  @Post(':id')
  async addFriend(@Param('id') id: string, @Body('friendId') friendId: string) {

    const first: number = Number(id);
    const second: number = Number(friendId);

    const first_add = await this.friendService.addFriend(first, second);
    const second_add = await this.friendService.addFriend(second, first);

    return {first_add, second_add};
  }

  @Delete(':id')
  async deleteFriend(@Param('id') id: string, @Body('friendId') friendId: string) {
    const first: number = Number(id);
    const second: number = Number(friendId);

    const first_deletion = await this.friendService.deleteFriend(first, second);
    const second_deletion = await this.friendService.deleteFriend(second, first);

    return {first_deletion, second_deletion};
  }
}