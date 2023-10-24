import { Module } from '@nestjs/common';
import { UserController } from './user.controller';
import { UserService } from './user.service';
import { PrismaService } from 'src/prisma/prisma.service';
import { FriendController } from './friend/friend.controller';
import { FriendService } from './friend/friend.service';

@Module({
  controllers: [UserController, FriendController],
  providers: [PrismaService, UserService, FriendService]
})
export class UserModule {}
