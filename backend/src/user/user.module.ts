import { Module } from '@nestjs/common';
import { UserController } from './user.controller';
import { UserService } from './user.service';
import { PrismaService } from 'src/prisma/prisma.service';
import { FriendController } from './friend/friend.controller';
import { FriendService } from './friend/friend.service';
import { BlockController } from './block/block.controller';
import { BlockService } from './block/block.service';

@Module({
  controllers: [UserController, FriendController, BlockController],
  providers: [PrismaService, UserService, FriendService, BlockService],
  exports: [UserService]
})
export class UserModule {}
